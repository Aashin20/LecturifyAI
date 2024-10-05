<template>
    <div class="wrapper">
        <div class="header" @click="$router.push('/')">
            <span class="left">
                <img src="../assets/logo.png" alt="logo" class="logo">
                <span class="f-row">
                    <h1 class="name">Lecturify</h1>
                    <h2 class="motto">Education Unlocked</h2>
                </span>
            </span>
            <img src="../assets/avatar.png" alt="avatar" class="avatar">
        </div>
            
            <h1 class="title">Access notes, material, & more</h1>
            <div class="lecture-card" id="lecture-card-1" @click="getPDF">
                    <span class="flex-wrapper">
                        <h1 class="lecture-title" >New Lecture 2 Detailed Notes</h1>
                        <h3 class="lecture-date"><span class="bolden">2</span> Pages ~ <span class="bolden">10</span> Minutes</h3>
                    </span>
            </div>
            <div class="lecture-card" id="lecture-card-2" @click="getCheatSheet">
                    <span class="flex-wrapper">
                        <h1 class="lecture-title">New Lecture 2 Bullet Points</h1>
                        <h3 class="lecture-date"><span class="bolden">1</span> Pages ~ <span class="bolden">4</span> Minutes</h3>
                    </span>
            </div>
            <div class="lecture-card" id="lecture-card-3" @click="$router.push('/cards')">
                    <span class="flex-wrapper">
                        <h1 class="lecture-title">Revise your learning - Flash Cards 101</h1>
                        <h3 class="lecture-date"><span class="bolden">8</span> Cards ~ <span class="bolden">8</span> Minutes</h3>
                    </span>
            </div>
            <div class="lecture-card" id="lecture-card-4" @click="$router.push('/quiz')">
                    <span class="flex-wrapper">
                        <h1 class="lecture-title">Test your knowledge - Quiz 101</h1>
                        <h3 class="lecture-date"><span class="bolden">10</span> Cards ~ <span class="bolden">5</span> Minutes</h3>
                    </span>
            </div>
</div>
</template>

<script setup>
import { useMainStore } from '@/stores/main';

const main = useMainStore()
const { getPDF, getCheatSheet, getFlashCards } = main;
</script>

<style scoped>
.wrapper {
    height: 100%;
    width: 100%;
    padding: 1rem 0.8rem;
    font-family: Poppins;
}

.header {
    display: flex;
    justify-content: space-between;
    margin-bottom: 1.5rem;
}

.left {
    display: flex;
    align-items: center;
}

.f-row {
    display: flex;
    flex-direction: column;
}

.logo {
    height: 3.3rem;
    width: 3.3rem;
    max-height: 3.3rem;
    max-width: 3.3rem;
    margin-right: 0.5rem;
}

.avatar {
    height: 3.3rem;
    width: 3.3rem;
    max-height: 3.3rem;
    max-width: 3.3rem;
}

.name {
    font-weight: 700;
    font-size: 1.2rem;
    margin-bottom: 0.3rem;
}

.motto {
    font-weight: 400;
    font-style: italic;
    font-size: 0.7rem;
}


.title {
    font-weight: 600;
    margin-bottom: 1rem;
}

.lecture-title {
    font-weight: 500;
    font-size: 0.8rem;
    margin-bottom: 0.4rem;
    width: 80%;
    line-height: 1.5rem;
}

.lecture-date {
    font-weight: 400;
    font-size: 0.6rem;
}

.bolden {
    font-weight: 600;
}

.lecture-tip {
    margin-top: 1rem;
    font-weight: 400;
    font-size: 0.8rem;
    color: #5EB670;
}

.lecture-card {
    background-color: #EFEFEF;
    padding: 1.7rem 1rem;
    border-radius: 0.4rem;
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 0.4rem;
}

#lecture-card-1{
    background-image: url(../assets/bg4.png);
    background-size: cover;
}

#lecture-card-2{
    background-image: url(../assets/bg5.png);
    background-size: cover;
}

#lecture-card-3{
    background-image: url(../assets/bg6.png);
    background-size: cover;
}

#lecture-card-4{
    background-image: url(../assets/bg7.png);
    background-size: cover;
}
</style>