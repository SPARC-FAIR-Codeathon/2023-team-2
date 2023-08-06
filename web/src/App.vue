<script setup lang="ts">
import { useHead } from '@unhead/vue'

useHead({
  title: 'SCKAN Visualizer',
  link: [
    {
      rel: 'icon',
      type: 'image/png',
      href: '/favicon.png'
    }
  ]
})
</script>

<template>
  <n-config-provider>
    <n-dialog-provider>
      <n-message-provider>
        <AppHeader />

        <div class="w-full h-full p-4">
          <router-view v-slot="{ Component }">
            <transition name="fade" appear mode="out-in">
              <component :is="Component" />
            </transition>
          </router-view>
        </div>
      </n-message-provider>
    </n-dialog-provider>
  </n-config-provider>
</template>
