<script setup lang="ts">
import cytoscape from 'cytoscape'
import { onMounted } from 'vue'

const init = () => {
  cytoscape({
    container: document.getElementById('cy'),
    elements: {
      nodes: [
        { data: { id: 'a' } },
        { data: { id: 'b', parent: 'parent' } },
        { data: { id: 'c', parent: 'parent' } },
        { data: { id: 'd' } },
        { data: { id: 'e' } },
        { data: { id: 'parent' } }
      ],
      edges: [
        {
          data: {
            id: 'ab',
            source: 'a',
            target: 'b'
          }
        },
        {
          data: {
            id: 'bc',
            source: 'b',
            target: 'd'
          }
        },
        {
          data: {
            id: 'cd',
            source: 'c',
            target: 'a'
          }
        },
        {
          data: {
            id: 'de',
            source: 'd',
            target: 'e'
          }
        },
        {
          data: {
            id: 'ea',
            source: 'e',
            target: 'a'
          }
        }
      ]
    },
    layout: {
      name: 'cose',
      animate: true
    },
    minZoom: 1,
    maxZoom: 2,

    // so we can see the ids
    style: [
      {
        selector: 'node',
        style: {
          label: 'data(id)'
        }
      }
    ]
  })
}

onMounted(() => {
  init()
})
</script>

<template>
  <div id="cy" class="border min-w-full h-[calc(100vh-200px)]"></div>
</template>
