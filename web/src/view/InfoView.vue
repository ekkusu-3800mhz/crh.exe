<script setup lang="ts">

import { ref } from 'vue';
import axios, { type AxiosResponse } from 'axios';
import type { IStreamInfo, IStreamInfoContent } from '@/interface/info';
import type { IQueueInfo } from '@/interface/queue';

/* 渲染常量定义 */

const infoList = ref<IStreamInfoContent[]>();
const queueInfo = ref<IQueueInfo>({
  maxCapacity: 0,
  cabinets: {
    left: {count: 0, updateTime: "0000-00-00 00:00:00"},
    right: {count: 0, updateTime: "0000-00-00 00:00:00"},
  },
});

/* 实用函数定义 */

const LI_OFFSET: number = 3;

function generateLi(sort: number): string {
    return `anim${sort + LI_OFFSET}`;
}

function parsePlayerCount(count: number): number {
  if (queueInfo.value.maxCapacity === 0) {
    return 0;
  }
  return count / queueInfo.value.maxCapacity;
  /*if (queueInfo.value.maxCapacity === 0) {
    return "/images/queue-0.png";
  }
  let percent: number = count / queueInfo.value.maxCapacity;
  if (percent > 0 || percent <= 0.2) {
    return "/images/queue-1.png";
  } else if (percent > 0.2 || percent <= 0.4) {
    return "/images/queue-2.png";
  } else if (percent > 0.4 || percent <= 0.6) {
    return "/images/queue-3.png";
  } else if (percent > 0.6 || percent <= 0.8) {
    return "/images/queue-4.png";
  } else if (percent > 0.8) {
    return "/images/queue-5.png";
  } else {
    return "/images/queue-0.png";
  }*/
}

/* 获取初始数据 */

axios({
  url: `/data/info.json?timestamp=${new Date().getTime()}`,
  method: 'GET',
}).then((res: AxiosResponse<IStreamInfo>) => {
  infoList.value = res.data.info;
});

axios({
  url: `/data/queue.json?timestamp=${new Date().getTime()}`,
  method: 'GET',
}).then((res: AxiosResponse<IQueueInfo>) => {
  queueInfo.value = res.data;
});

/* 定时获取数据 */

const INFO_REFRESH_INT = 60000;
const QUEUE_REFRESH_INT = 15000;

const infoInterval = setInterval(() => {
  axios({
    url: `/data/info.json?timestamp=${new Date().getTime()}`,
    method: 'GET',
  }).then((res: AxiosResponse<IStreamInfo>) => {
    infoList.value = res.data.info;
  });
}, INFO_REFRESH_INT);

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
  <div class="content-slider">
    <div class="slider">
      <div class="mask">
        <ul>
          <li class="anim1">
            <div class="quote">
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
              [当前排队人数参考]<br>
              非直播机（1P/2P）：{{queueInfo.cabinets.left.count}}人（基于玩家群体更新，会有滞后性）
            </div>
          </li>
          <li class="anim2">
            <div class="quote">
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
              [当前排队人数参考]<br>
              直播机（3P/4P）：{{queueInfo.cabinets.right.count}}人（基于玩家群体更新，会有滞后性）
            </div>
          </li>
          <li v-for="(text, index) in infoList" :class="generateLi(index)">
            <div class="quote" v-html="text.content"></div>
          </li>
        </ul>
      </div>
    </div>
  </div>
</template>

<style scoped>
h1 {
  font-size: 60px;
  text-align: center;
}

img.player-count-img {
  float: left;
  margin: 6px;
  height: 60px;
}

.content-slider {
  width: 960px;
  height: 80px;
}

.slider {
  height: 80px;
  width: 960px;
  overflow: visible;
  position: relative;
}

.mask {
  overflow: hidden;
  height: 80px;
}

.slider ul {
  margin: 0;
  padding: 0;
  position: relative;
}

.slider li {
  width: 960px;
  height: 80px;
  position: absolute;
  top: -85px;
  list-style: none;
}

.slider .quote {
  font-size: 24px;
  font-style: normal;
  color: #ffffff;
  text-shadow: #153644 0px 0px 4px;
}

.slider .source {
  font-size: 24px;
  text-align: right;
}

.slider li.anim1 {
  animation: cycle 15s linear infinite;
}

.slider li.anim2 {
  animation: cycle2 15s linear infinite;
}

.slider li.anim3 {
  animation: cycle3 15s linear infinite;
}

.slider li.anim4 {
  animation: cycle4 15s linear infinite;
}

.slider li.anim5 {
  animation: cycle5 15s linear infinite;
}

.slider li.anim6 {
  animation: cycle6 15s linear infinite;
}

.slider li.anim7 {
  animation: cycle7 15s linear infinite;
}

@keyframes cycle {
  0% { top: 0px; }
  4% { top: 0px; }
  16% { top: 0px; opacity: 1; z-index: 0; }
  20% { top: 85px; opacity: 0; z-index: 0; }
  21% { top: -85px; opacity: 0; z-index: -1; }
  50% { top: -85px; opacity: 0; z-index: -1; }
  92% { top: -85px; opacity: 0; z-index: 0; }
  96% { top: -85px; opacity: 0; }
  100% { top: 0px; opacity: 1; }
}

@keyframes cycle2 {
  0% {top: -85px;opacity: 0;}
  16% {top: -85px;opacity: 0;}
  20% {top: 0px;opacity: 1;}
  24% {top: 0px;opacity: 1;}
  36% {top: 0px;opacity: 1;z-index: 0;}
  40% {top: 85px;opacity: 0;z-index: 0;}
  41% {top: -85px;opacity: 0;z-index: -1;}
  100% {top: -85px;opacity: 0;z-index: -1;}
}

@keyframes cycle3 {
  0% {top: -85px;opacity: 0;}
  36% {top: -85px;opacity: 0;}
  40% {top: 0px;opacity: 1;}
  44% {
    top: 0px;
    opacity: 1;
  }
  56% {
    top: 0px;
    opacity: 1;
    z-index: 0;
  }
  60% {
    top: 85px;
    opacity: 0;
    z-index: 0;
  }
  61% {
    top: -85px;
    opacity: 0;
    z-index: -1;
  }
  100% {
    top: -85px;
    opacity: 0;
    z-index: -1;
  }
}

@keyframes cycle4 {
  0% {
    top: -85px;
    opacity: 0;
  }
  56% {
    top: -85px;
    opacity: 0;
  }
  60% {
    top: 0px;
    opacity: 1;
  }
  64% {
    top: 0px;
    opacity: 1;
  }
  76% {
    top: 0px;
    opacity: 1;
    z-index: 0;
  }
  80% {
    top: 85px;
    opacity: 0;
    z-index: 0;
  }
  81% {
    top: -85px;
    opacity: 0;
    z-index: -1;
  }
  100% {
    top: -85px;
    opacity: 0;
    z-index: -1;
  }
}

@keyframes cycle5 {
  0% {
    top: -85px;
    opacity: 0;
  }
  76% {
    top: -85px;
    opacity: 0;
  }
  80% {
    top: 0px;
    opacity: 1;
  }
  84% {
    top: 0px;
    opacity: 1;
  }
  96% {
    top: 0px;
    opacity: 1;
    z-index: 0;
  }
  100% {
    top: 85px;
    opacity: 0;
    z-index: 0;
  }
}
</style>