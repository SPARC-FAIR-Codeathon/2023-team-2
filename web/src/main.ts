import './assets/main.css'

import { Icon } from '@iconify/vue'
import { createApp } from 'vue'
import { createPinia } from 'pinia'
import { createHead } from '@unhead/vue'
import Vue3Lottie from 'vue3-lottie'

import App from './App.vue'
import router from './router'

const app = createApp(App)

const head = createHead()

app.component('f-icon', Icon)

app.use(head)
app.use(createPinia())
app.use(router)
app.use(Vue3Lottie)

app.mount('#app')
