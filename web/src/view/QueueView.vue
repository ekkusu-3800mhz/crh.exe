<script setup lang="ts">

import { ref } from 'vue';
import axios, { type AxiosResponse } from 'axios';
import type { IQueueInfo, IQueueInfoRow } from '@/interface/queue';

/* 渲染常量定义 */

const queueInfo = ref<IQueueInfoRow[]>([]);

/* 实用函数定义 */

function parsePlayerCount(playerCount: number, number: number, maxCapacity: number): number {
  if (maxCapacity === 0) {
    return 0;
  }
  return playerCount / (number * maxCapacity);
}

function calculateTimeDiff(timestamp: string): boolean {
  let cabinetTimestamp = new Date(timestamp);
  let currentTimestamp = new Date();
  return (((currentTimestamp.getTime() - cabinetTimestamp.getTime()) / 1000) > 3600);
}

/* 获取初始数据 */

axios({
  url: `http://widgets.live.qymai.xbuster.moe:12724/bot/queue_info?timestamp=${new Date().getTime()}`,
  method: 'GET',
}).then((res: AxiosResponse<IQueueInfo>) => {
  if (!res.data.data.error) {
    queueInfo.value = res.data.data.cabinetList;
  }
});

/* 定时获取数据 */

const QUEUE_REFRESH_INT = 5000;

const queueInterval = setInterval(() => {
  axios({
    url: `http://widgets.live.qymai.xbuster.moe:12724/bot/queue_info?timestamp=${new Date().getTime()}`,
    method: 'GET',
  }).then((res: AxiosResponse<IQueueInfo>) => {
    if (!res.data.data.error) {
      queueInfo.value = res.data.data.cabinetList;
    }
  });
}, QUEUE_REFRESH_INT);

</script>

<template>
  <ul>
    <li v-for="cabinet in queueInfo">
      <template v-if="parsePlayerCount(cabinet.playerCount, cabinet.number, cabinet.maxCapacity) <= 0">
        <img src="/images/queue-0.png" class="player-count-img" alt="拥挤度">
      </template>
      <template v-else-if="parsePlayerCount(cabinet.playerCount, cabinet.number, cabinet.maxCapacity) > 0 && parsePlayerCount(cabinet.playerCount, cabinet.number, cabinet.maxCapacity) <= 0.2">
        <img src="/images/queue-1.png" class="player-count-img" alt="拥挤度">
      </template>
      <template v-else-if="parsePlayerCount(cabinet.playerCount, cabinet.number, cabinet.maxCapacity) > 0.2 && parsePlayerCount(cabinet.playerCount, cabinet.number, cabinet.maxCapacity) <= 0.4">
        <img src="/images/queue-2.png" class="player-count-img" alt="拥挤度">
      </template>
      <template v-else-if="parsePlayerCount(cabinet.playerCount, cabinet.number, cabinet.maxCapacity) > 0.4 && parsePlayerCount(cabinet.playerCount, cabinet.number, cabinet.maxCapacity) <= 0.6">
        <img src="/images/queue-3.png" class="player-count-img" alt="拥挤度">
      </template>
      <template v-else-if="parsePlayerCount(cabinet.playerCount, cabinet.number, cabinet.maxCapacity) > 0.6 && parsePlayerCount(cabinet.playerCount, cabinet.number, cabinet.maxCapacity) <= 0.8">
        <img src="/images/queue-4.png" class="player-count-img" alt="拥挤度">
      </template>
      <template v-else-if="parsePlayerCount(cabinet.playerCount, cabinet.number, cabinet.maxCapacity) > 0.8">
        <img src="/images/queue-5.png" class="player-count-img" alt="拥挤度">
      </template>
      {{cabinet.name}}<br>
      {{cabinet.playerCount}}人
      <template v-if="calculateTimeDiff(cabinet.updateTime)">
        <span class="expire-notice">[时效性注意]</span>
      </template>
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

li > span.expire-notice {
  color: #fff200;
}

img.player-count-img {
  float: left;
  margin: 6px;
  height: 35px;
}
</style>