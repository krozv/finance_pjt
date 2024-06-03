<template>
    <v-card
        :subtitle=item.bank
        :title=item.title
        text="상품설명"    
    >
    </v-card>
</template>

<script setup>
const props = defineProps({
    item: Object
})
</script>

<style scoped>

</style>