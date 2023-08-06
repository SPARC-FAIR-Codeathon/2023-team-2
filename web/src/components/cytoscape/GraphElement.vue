<script setup lang="ts">
import cytoscape from 'cytoscape'
import { onMounted } from 'vue'

const DrawerActive = ref(false)

const DrawerData = ref({
  title: '',
  content: ''
})

const init = () => {
  const cy = cytoscape({
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
      },
      {
        selector: 'edge',
        style: {
          width: 2,
          'line-color': '#ccc',
          'target-arrow-color': '#000',
          'target-arrow-shape': 'triangle',
          'curve-style': 'bezier'
        }
      }
    ]
  })

  cy.on('tap', 'node', (evt) => {
    var node = evt.target
    console.log('tapped ' + node.id())

    DrawerData.value.title = `Data for node ${node.id()}`

    DrawerActive.value = true
  })

  cy.on('tap', 'edge', (evt) => {
    var edge = evt.target
    console.log('tapped ' + edge.id())

    DrawerData.value.title = `Data for edge ${edge.id()}`

    DrawerActive.value = true
  })
}

onMounted(() => {
  init()
})
</script>

<template>
  <div>
    <div id="cy" class="border min-w-full h-[calc(100vh-200px)]"></div>

    <n-drawer
      v-model:show="DrawerActive"
      default-width="30%"
      placement="right"
      :resizable="true"
      :auto-focus="true"
    >
      <n-drawer-content :title="DrawerData.title" closable>
        Lorem ipsum dolor sit amet consectetur adipisicing elit. Quisquam, quos. Quisquam, quos.
      </n-drawer-content>
    </n-drawer>
  </div>
</template>
