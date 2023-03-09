<script setup lang="ts">

import { ref } from 'vue';
import axios, { type AxiosResponse } from 'axios';
import type { IStreamInfo, IStreamInfoContent } from '@/interface/info';

/* 渲染常量定义 */

const infoList = ref<IStreamInfoContent[]>();

/* 实用函数定义 */

const LI_OFFSET: number = 1;

function generateLi(sort: number): string {
    return `anim${sort + LI_OFFSET}`;
}

/* 获取初始数据 */

axios({
  url: `/data/info.json?timestamp=${new Date().getTime()}`,
  method: 'GET',
}).then((res: AxiosResponse<IStreamInfo>) => {
  infoList.value = res.data.info;
});

/* 定时获取数据 */

const INFO_REFRESH_INT = 60000;

const infoInterval = setInterval(() => {
  axios({
    url: `/data/info.json?timestamp=${new Date().getTime()}`,
    method: 'GET',
  }).then((res: AxiosResponse<IStreamInfo>) => {
    infoList.value = res.data.info;
  });
}, INFO_REFRESH_INT);

</script>

<template>
  <div class="content-slider">
    <div class="slider">
      <div class="mask">
        <ul>
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

@keyframes cycle {
  0% {
    top: 0px;
  }
  4% {
    top: 0px;
  }
  16% {
    top: 0px;
    opacity: 1;
    z-index: 0;
  }
  20% {
    top: 85px;
    opacity: 0;
    z-index: 0;
  }
  21% {
    top: -85px;
    opacity: 0;
    z-index: -1;
  }
  50% {
    top: -85px;
    opacity: 0;
    z-index: -1;
  }
  92% {
    top: -85px;
    opacity: 0;
    z-index: 0;
  }
  96% {
    top: -85px;
    opacity: 0;
  }
  100% {
    top: 0px;
    opacity: 1;
  }
}

@keyframes cycle2 {
  0% {
    top: -85px;
    opacity: 0;
  }
  16% {
    top: -85px;
    opacity: 0;
  }
  20% {
    top: 0px;
    opacity: 1;
  }
  24% {
    top: 0px;
    opacity: 1;
  }
  36% {
    top: 0px;
    opacity: 1;
    z-index: 0;
  }
  40% {
    top: 85px;
    opacity: 0;
    z-index: 0;
  }
  41% {
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

@keyframes cycle3 {
  0% {
    top: -85px;
    opacity: 0;
  }
  36% {
    top: -85px;
    opacity: 0;
  }
  40% {
    top: 0px;
    opacity: 1;
  }
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