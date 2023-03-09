<script setup lang="ts">

import { ref } from 'vue';
import axios, { type AxiosResponse } from 'axios';
import type { IQueueInfo } from '@/interface/queue';

/* 渲染常量定义 */

const queueInfo = ref<IQueueInfo>({
  maxCapacity: 0,
  cabinets: {
    left: {count: 0, updateTime: "0000-00-00 00:00:00"},
    right: {count: 0, updateTime: "0000-00-00 00:00:00"},
  },
});

/* 实用函数定义 */

function parsePlayerCount(count: number): number {
  if (queueInfo.value.maxCapacity === 0) {
    return 0;
  }
  return count / queueInfo.value.maxCapacity;
}

/* 获取初始数据 */

axios({
  url: `/data/queue.json?timestamp=${new Date().getTime()}`,
  method: 'GET',
}).then((res: AxiosResponse<IQueueInfo>) => {
  queueInfo.value = res.data;
});

/* 定时获取数据 */

const QUEUE_REFRESH_INT = 15000;

const queueInterval = setInterval(() => {
  axios({
    url: `/data/queue.json?timestamp=${new Date().getTime()}`,
    method: 'GET',
  }).then((res: AxiosResponse<IQueueInfo>) => {
    queueInfo.value = res.data;
  });
}, QUEUE_REFRESH_INT);

</script>

<template>
  <ul>
    <li>
      <template v-if="parsePlayerCount(queueInfo.cabinets.left.count) <= 0">
        <img src="/images/queue-0.png" class="player-count-img" alt="拥挤度">
      </template>
      <template v-else-if="parsePlayerCount(queueInfo.cabinets.left.count) > 0 && parsePlayerCount(queueInfo.cabinets.left.count) <= 0.2">
        <img src="/images/queue-1.png" class="player-count-img" alt="拥挤度">
      </template>
      <template v-else-if="parsePlayerCount(queueInfo.cabinets.left.count) > 0.2 && parsePlayerCount(queueInfo.cabinets.left.count) <= 0.4">
        <img src="/images/queue-2.png" class="player-count-img" alt="拥挤度">
      </template>
      <template v-else-if="parsePlayerCount(queueInfo.cabinets.left.count) > 0.4 && parsePlayerCount(queueInfo.cabinets.left.count) <= 0.6">
        <img src="/images/queue-3.png" class="player-count-img" alt="拥挤度">
      </template>
      <template v-else-if="parsePlayerCount(queueInfo.cabinets.left.count) > 0.6 && parsePlayerCount(queueInfo.cabinets.left.count) <= 0.8">
        <img src="/images/queue-4.png" class="player-count-img" alt="拥挤度">
      </template>
      <template v-else-if="parsePlayerCount(queueInfo.cabinets.left.count) > 0.8">
        <img src="/images/queue-5.png" class="player-count-img" alt="拥挤度">
      </template>
      牛仔城非直播机<br>
      {{queueInfo.cabinets.left.count}}人
    </li>
    <li>
      <template v-if="parsePlayerCount(queueInfo.cabinets.right.count) <= 0">
        <img src="/images/queue-0.png" class="player-count-img" alt="拥挤度">
      </template>
      <template v-else-if="parsePlayerCount(queueInfo.cabinets.right.count) > 0 && parsePlayerCount(queueInfo.cabinets.right.count) <= 0.2">
        <img src="/images/queue-1.png" class="player-count-img" alt="拥挤度">
      </template>
      <template v-else-if="parsePlayerCount(queueInfo.cabinets.right.count) > 0.2 && parsePlayerCount(queueInfo.cabinets.right.count) <= 0.4">
        <img src="/images/queue-2.png" class="player-count-img" alt="拥挤度">
      </template>
      <template v-else-if="parsePlayerCount(queueInfo.cabinets.right.count) > 0.4 && parsePlayerCount(queueInfo.cabinets.right.count) <= 0.6">
        <img src="/images/queue-3.png" class="player-count-img" alt="拥挤度">
      </template>
      <template v-else-if="parsePlayerCount(queueInfo.cabinets.right.count) > 0.6 && parsePlayerCount(queueInfo.cabinets.right.count) <= 0.8">
        <img src="/images/queue-4.png" class="player-count-img" alt="拥挤度">
      </template>
      <template v-else-if="parsePlayerCount(queueInfo.cabinets.right.count) > 0.8">
        <img src="/images/queue-5.png" class="player-count-img" alt="拥挤度">
      </template>
      牛仔城直播机<br>
      {{queueInfo.cabinets.right.count}}人
    </li>
  </ul>
</template>

<style scoped>
ul {
  margin-left: -40px;
  width: 260px;
  height: 340px;
  overflow: hidden;
}

li {
  list-style: none;
  font-size: 16px;
  font-style: normal;
  color: #ffffff;
  text-shadow: #153644 0px 0px 4px;
  padding-bottom: 10px;
}

img.player-count-img {
  float: left;
  margin: 6px;
  height: 35px;
}
</style>