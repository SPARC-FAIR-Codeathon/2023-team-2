<script setup lang="ts">
import { API_URL } from '@/utils/constants'

const neuronModules = ref<string[]>([])
const showVisualization = ref(false)
const loading = ref(false)

const visualizationData = ref({})

const { info, error } = useMessage()

const submitModels = async () => {
  loading.value = true
  showVisualization.value = false

  const neurons: string[] = []

  for (const neuron of neuronModules.value) {
    if (neuron === '') continue

    neurons.push(neuron)
  }

  if (neurons.length === 0) {
    error('Please add at least one neuron module')

    // loading.value = false

    // return
  }

  // remove duplicates
  const uniqueNeurons = [...new Set(neurons)]

  const length = uniqueNeurons.length

  info(`Generating visualization for ${length} neuron${length > 1 ? 's' : ''}`)

  setTimeout(async () => {
    const response = await fetch(`${API_URL}/generate`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        neurons: uniqueNeurons
      })
    })

    const json = await response.json()

    visualizationData.value = json

    loading.value = false
    showVisualization.value = true
  }, 10)
}
</script>

<template>
  <div class="graph-container h-full w-full">
    <div class="flex items-center space-x-4">
      <h2>Which neuron modules would you like to visualize?</h2>

      <div>
        <n-dynamic-tags v-model:value="neuronModules" type="info">
          <template #trigger="{ activate }">
            <n-button size="small" type="primary" dashed @click="activate()">
              <template #icon>
                <f-icon icon="carbon:add-filled" />
              </template>

              Add Neuron
            </n-button>
          </template>
        </n-dynamic-tags>
      </div>

      <n-divider vertical />

      <n-button type="info" strong size="small" :loading="loading" @click="submitModels">
        <template #icon>
          <f-icon icon="pixelarticons:play" />
        </template>
        Visualize
      </n-button>
    </div>

    <n-collapse-transition :show="showVisualization">
      <n-divider />

      <GraphElement :visualizationData="visualizationData" :key="visualizationData" />
    </n-collapse-transition>
  </div>
</template>
