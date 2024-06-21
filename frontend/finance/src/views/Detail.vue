<template>
    <div class="mx-16 mt-4">
        <div class="d-flex">
        <h2 class="fontStyle">{{ item.title }}</h2>
        <h2>
        &nbsp;상품을 찾으시나요?
        </h2>
        </div>
        <v-row class="mt-1">
            <v-col cols="6">
                <ClassificationComponent :item = item></ClassificationComponent>
            </v-col>
            <v-col cols="6">
                <MapComponent>
                </MapComponent>
            </v-col>
        </v-row>
    </div>
</template>

<script setup>
import ClassificationComponent from '@/components/ClassificationComponent.vue'
import MapComponent from '@/components/MapComponent.vue'

const item = JSON.parse(localStorage.getItem('item'))

// 해당 router 에서 나갈 시 itemStore.clear 해야 함!!!

</script>

<style scoped>
.fontStyle {
    color: white;
}
.fontStyle:hover {
    text-decoration: underline;
}
</style>