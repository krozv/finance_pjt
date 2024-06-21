<template>
    <v-card
        color="#D9D9D9"
        :subtitle=item.bank
        :title=item.title
        text="상품설명"
        @click="moveTo(item)" 
    >
    </v-card>
</template>

<script setup>
import { useRouter } from 'vue-router'
import { useItemStore } from '@/stores/item';

const props = defineProps({
    item: Object
})

// router 활용해서 detail views 로 이동
const router = useRouter()
// pinia에 item 정보 저장하기
const itemStore = useItemStore()
const moveTo = function (item) {
    itemStore.setItem(item)
    router.push({ name: 'detail' })
}


</script>

<style scoped>

</style>