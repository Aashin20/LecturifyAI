<template>
    <div class="wrapper">
        <div class="header">
            <span class="left">
                <img src="../assets/logo.png" alt="logo" class="logo">
                <span class="f-row">
                    <h1 class="name">Lecturify</h1>
                    <h2 class="motto">Education Unlocked</h2>
                </span>
            </span>
            <img src="../assets/avatar.png" alt="avatar" class="avatar">
        </div>
            <img src="../assets/banner1.png" alt="banner-1" class="banner-1" @click="$router.push('/record')">
            <h1 class="title">Your courses</h1>
            <div class="scroll-wrapper">
                <div class="scroll-item" id="scroll-item-1">
                    <div class="text-wrapper">
                        <h1 class="subject">Physics</h1>
                        <h2 class="code">21PHY101T</h2>
                        <div class="completion-bar">
                            <div class="completion-bar-inside" style="width: 90%;"></div>
                        </div>
                    </div>
                </div>
                <div class="scroll-item" id="scroll-item-2">
                    <div class="text-wrapper">
                        <h1 class="subject">History</h1>
                        <h2 class="code">21HIT201T</h2>
                        <div class="completion-bar">
                            <div class="completion-bar-inside" style="width: 40%;"></div>
                        </div>
                    </div>
                </div>
                <div class="scroll-item" id="scroll-item-3">
                    <div class="text-wrapper">
                        <h1 class="subject">Computer Sc..</h1>
                        <h2 class="code">21CSC101J</h2>
                        <div class="completion-bar">
                            <div class="completion-bar-inside" style="width: 30%;"></div>
                        </div>
                    </div>
                </div>
            </div>
            <h1 class="title">Continue learning</h1>
            <div class="lecture-card" @click="$router.push('/content')">
                    <span class="flex-wrapper">
                        <h1 class="lecture-title">New Lecture Recording</h1>
                        <h3 class="lecture-date">Recorded on 01/10/2024</h3>
                        <h3 class="lecture-tip">Flash cards available</h3>
                    </span>
                    <img src="../assets/play.png" alt="play" class="play">
            </div>
            <div class="lecture-card">
                    <span class="flex-wrapper">
                        <h1 class="lecture-title">Harmonic Analysis L1</h1>
                        <h3 class="lecture-date">Recorded on 29/09/2024</h3>
                    </span>
                    <img src="../assets/play.png" alt="play" class="play">
            </div>
            <div class="lecture-card">
                    <span class="flex-wrapper">
                        <h1 class="lecture-title">Second Order Derivat...</h1>
                        <h3 class="lecture-date">Recorded on 26/09/2024</h3>
                    </span>
                    <img src="../assets/play.png" alt="play" class="play">
            </div>
</div>
</template>

<script setup></script>

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

.banner-1 {
    width: 100%;
    margin-bottom: 1.5rem;
}

.scroll-wrapper {
    overflow-y: hidden;
    overflow: auto;
    white-space: nowrap;
    height: 12.5rem;
    margin-bottom: 1.5rem;
    -ms-overflow-style: none;  /* Internet Explorer 10+ */
    scrollbar-width: none;  /* Firefox */
}

.scroll-wrapper::-webkit-scrollbar { 
    display: none;  /* Safari and Chrome */
}

.scroll-item {
    width: 12rem;
    height: 12.4rem;
    border-radius: 0.4rem;
    display: inline-block;
    flex-direction: column;
    background-size: cover;
    margin-right: 0.5rem;
    white-space: nowrap;
    background-color: #f4f4f4;
  overflow: hidden;
  text-overflow: ellipsis;
}

.title {
    font-weight: 600;
    margin-bottom: 1rem;
}

.subject {
    margin-top: 2rem;
    margin-left: 1rem;
    margin-bottom: 0.5rem;
    font-weight: 600;
    font-size: 1.2rem
}

.code {
    margin-left: 1rem;
    margin-bottom: 0.5rem;
    font-weight: 400;
    font-size: 0.8rem;
}

.completion-bar {
    height: 0.5rem;
    width: 70%;
    background-color: #D9D9D9;
    border-radius: 0.6rem;
    margin-left: 1rem;
}

.completion-bar-inside {
    height: 0.5rem;
    background-color: #5EB670;
    border-radius: 0.6rem 0 0 0.6rem;
}

#scroll-item-1 {
    background-image: url(../assets/bg1.png);
}

#scroll-item-2 {
    background-image: url(../assets/bg2.png);
}

#scroll-item-3 {
    background-image: url(../assets/bg3.png);
}

.lecture-title {
    font-weight: 500;
    font-size: 1rem;
    margin-bottom: 0.4rem;
}

.lecture-date {
    font-weight: 400;
    font-size: 0.7rem;
}

.lecture-tip {
    margin-top: 1rem;
    font-weight: 400;
    font-size: 0.8rem;
    color: #5EB670;
}

.lecture-card {
    background-color: #EFEFEF;
    padding: 1.4rem 1rem;
    border-radius: 0.4rem;
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 0.4rem;
}

.play {
    height: 2.5rem;
}
</style>