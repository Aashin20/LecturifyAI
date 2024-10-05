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
      <div class="box">
        <div class="pulsating-circle" @click="runSpeechRecog" v-show="isActive" @style="{}"></div>
          <img src="../assets/mic.png" @click="runSpeechRecog" alt="Start Recording" class="mic">
        
          <h1 class="title">New Session Recording</h1>
          <h3 class="subtitle" v-if="isActive">Press icon to stop recording</h3>
          <h3 class="subtitle" v-if="!isActive">Press icon to start recording</h3>
          <h4 class="text">{{speechRecog}}...</h4>
      </div>
  </div>
</template>

<script setup>
import { useMainStore } from '@/stores/main';
import { ref } from 'vue';
import { useRouter } from 'vue-router';
const router = useRouter()

const main = useMainStore()
const { addTranscript } = main;

let speechRecog = ref("")
const isActive = ref(false)

function runSpeechRecog() {
  let recognization = new webkitSpeechRecognition();
  recognization.continuous = true;
  isActive.value = !isActive.value;
  recognization.interimResults = false; 

  let lastTranscript = '';

  recognization.onresult = (e) => {
      var transcript = e.results[e.results.length - 1][0].transcript.trim(); // Get the latest result
      if (transcript !== lastTranscript) { // Only log if it's different
          lastTranscript += " " + transcript; // Update lastTranscript
          speechRecog.value = lastTranscript.trim().split(/\s+/).slice(-20).join(' ');
      }
  };

  recognization.onend = () => {
      console.log('Speech recognition service disconnected');
      addTranscript(lastTranscript);
      setTimeout(() => {
        router.push('/')
}, 1000);
      
  };

  recognization.start();
}

</script>

<style scoped>
.text {
margin-top: 5rem;
line-height: 0.8rem;
font-size: 0.8rem;
text-align: center;
color: #3f3f3f;
padding: 0 1rem;
}

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
  top: 60%;
  right: -530%;
  position: absolute;
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

.box {
  height: 75vh;
  border-radius: 0.4rem;
  display: flex;
  justify-content: center;
  align-items: center;
  flex-direction: column;
  width: 100%;
  background-color: #EFEFEF;
}

.title {
margin-top: 2rem;
  font-weight: 600;
  font-size: 0.8rem;
  margin-bottom: 0.4rem;
}

.subtitle {
  font-weight: 400;
  font-size: 0.6rem;
}

.mic {
  height: 5rem;
}

.pulsating-circle {
width: 50px;
height: 50px;
}

.pulsating-circle:before {
margin-left: -100%;
margin-top: 30%;
content: "";
display: block;
width: 300%;
height: 300%;
box-sizing: border-box;
border-radius: 100%;
background-color: #5EB670;
-webkit-animation: pulse-ring 1.25s cubic-bezier(0.215, 0.61, 0.355, 1) infinite;
animation: pulse-ring 1.25s cubic-bezier(0.215, 0.61, 0.355, 1) infinite;
}
.pulsating-circle:after {
content: "";
margin-left: -100%;
margin-top: 30%;
display: none;
width: 100%;
height: 100%;
border-radius: 100%;
box-shadow: 0 0 8px rgba(0, 0, 0, 0.3);
-webkit-animation: pulse-dot 1.25s cubic-bezier(0.455, 0.03, 0.515, 0.955) -0.4s infinite;
        animation: pulse-dot 1.25s cubic-bezier(0.455, 0.03, 0.515, 0.955) -0.4s infinite;
}

@-webkit-keyframes pulse-ring {
0% {
  transform: scale(0.33);
}
80%, 100% {
  opacity: 0;
}
}

@keyframes pulse-ring {
0% {
  transform: scale(0.33);
}
80%, 100% {
  opacity: 0;
}
}
@-webkit-keyframes pulse-dot {
0% {
  transform: scale(0.8);
}
50% {
  transform: scale(1);
}
100% {
  transform: scale(0.8);
}
}
@keyframes pulse-dot {
0% {
  transform: scale(0.8);
}
50% {
  transform: scale(1);
}
100% {
  transform: scale(0.8);
}
}
</style>