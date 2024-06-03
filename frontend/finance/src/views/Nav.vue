<template>
    <v-toolbar>
        <v-btn @click="moveTo('home')">
            서비스명
        </v-btn>
        <v-spacer></v-spacer>
        <v-btn @click="moveTo('deposit')">
            예금
        </v-btn>
        <v-spacer></v-spacer>
        <v-btn @click="moveTo('savings')">
            적금
        </v-btn>
        <v-spacer></v-spacer>
        <v-btn @click="moveTo('exchange')">
            환율
        </v-btn>
        <v-spacer></v-spacer>
        <v-btn @click="moveTo('myPage')">
            마이페이지
        </v-btn>
    </v-toolbar>
    <router-view></router-view>
</template>

<script setup>
import { useRouter } from 'vue-router'
const router = useRouter()

// router 이동
const moveTo = function (name) {
    router.push({ name: name })
}
</script>

<style scoped>

</style>