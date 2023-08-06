<script setup lang="ts">
import HOME_LOTTIE_JSON from '@/assets/animations/home.json'
</script>

<template>
  <main class="w-full h-full flex justify-center max-w-screen-lg mx-auto items-center">
    <div class="flex flex-col mr-[30px]">
      <h1 class="mt-10">
        <span class="text-5xl font-bold">SCKAN </span>

        <span class="text-5xl font-medium"> Visualizer</span>
      </h1>

      <p class="text-2xl py-4">
        Visualizing Neuronal Populations by using the existing neurondm python library for neurons
        and circuits curated in SCKAN (for example, neurons curated in SCKAN Composer), with variety
        of visualization tools such as cytoscape or d3
      </p>

      <div class="flex">
        <RouterLink :to="{ name: 'visualize' }">
          <n-button type="info" strong size="large">
            <template #icon>
              <f-icon icon="pixelarticons:play" />
            </template>
            Visualize
          </n-button>
        </RouterLink>
      </div>
    </div>

    <div>
      <Vue3Lottie :animationData="HOME_LOTTIE_JSON" :width="300" :height="300" />
    </div>
  </main>
</template>
