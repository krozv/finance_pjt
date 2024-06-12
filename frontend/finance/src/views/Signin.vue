<template>
    <v-card class="mx-auto mt-10" max-width="350" title="회원가입">
        <v-container>
            <v-text-field
            v-model="email"
            :rules="[required]"
            label="Email"
            placeholder="Enter your email"
            clearable
            ></v-text-field>
            <v-text-field
            v-model="nickname"
            :rules="[required]"
            label="Nickname"
            placeholder="Enter your nickname"
            clearable
            ></v-text-field>
            <v-text-field
            v-model="password"
            :rules="[required]"
            type="password"
            label="Password"
            placeholder="Enter your password"
            clearable
            ></v-text-field>
            <v-text-field
            v-model="confirmPassword"
            :rules="[required]"
            type="password"
            label="Confirm Password"
            placeholder="Please enter your password again"
            clearable
            ></v-text-field>
        </v-container>
        <v-divider></v-divider>
        <v-card-actions>
            <v-spacer></v-spacer>
            <v-btn
            type="submit"
            @click="signin">
                Sign in
            </v-btn>
        </v-card-actions>
    </v-card>
</template>

<script setup>
import { ref } from 'vue'

const required = function (v) {
    return !!v || 'Field is required'
}

const email = ref(null)
const nickname = ref(null)
const password = ref(null)
const confirmPassword = ref(null)

// 회원가입 요청 버튼
const signin = function () {

}
</script>

<style scoped>

</style>