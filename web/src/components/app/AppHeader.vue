<script setup lang="ts"></script>

<template>
  <header class="px-4 py-4 flex justify-between items-center border-b">
    <RouterLink :to="{ name: 'home' }">
      <h1 class="text-slate-700 hover:text-cyan-500 transition-all">SCKAN Visualizer</h1>
    </RouterLink>

    <div class="flex space-x-4 items-center">
      <RouterLink :to="{ name: 'visualize' }">
        <div class="text-xl font-semibold text-slate-600 hover:text-cyan-600 transition-all">
          Visualize
        </div>
      </RouterLink>

      <RouterLink :to="{ name: 'about' }">
        <div class="text-xl font-semibold text-slate-600 hover:text-cyan-600 transition-all">
          About
        </div>
      </RouterLink>
    </div>
  </header>
</template>
