<script setup>
import { RouterView } from 'vue-router'

</script>

<template>
  <RouterView />
</template>

<style>
/* CSS Reset */
html,
body,
div,
span,
applet,
object,
iframe,
h1,
h2,
h3,
h4,
h5,
h6,
p,
blockquote,
pre,
a,
abbr,
acronym,
address,
big,
cite,
code,
del,
dfn,
em,
img,
ins,
kbd,
q,
s,
samp,
small,
strike,
strong,
sub,
sup,
tt,
var,
b,
u,
i,
center,
dl,
dt,
dd,
ol,
ul,
li,
fieldset,
form,
label,
legend,
table,
caption,
tbody,
tfoot,
thead,
tr,
th,
td,
article,
aside,
canvas,
details,
embed,
figure,
figcaption,
footer,
header,
hgroup,
menu,
nav,
output,
ruby,
section,
summary,
time,
mark,
audio,
video {
	margin: 0;
	padding: 0;
	border: 0;
	font-size: 100%;
	font: inherit;
	vertical-align: baseline;
}

* {
	box-sizing: border-box;
	-webkit-box-sizing: border-box;
	-moz-box-sizing: border-box;
	-webkit-tap-highlight-color: rgba(0, 0, 0, 0);
  font-family: Poppins;
}

a {
	text-decoration: none;
}

/* HTML5 display-role reset for older browsers */
article,
aside,
details,
figcaption,
figure,
footer,
header,
hgroup,
menu,
nav,
section {
	display: block;
}

body {
	line-height: 1;
}

ol,
ul {
	list-style: none;
}

blockquote,
q {
	quotes: none;
}

blockquote:before,
blockquote:after,
q:before,
q:after {
	content: "";
	content: none;
}

table {
	border-collapse: collapse;
	border-spacing: 0;
}

/* Fonts */
@font-face {
	font-family: "Poppins";
	src: local("Poppins"), url(./fonts/poppins-300.woff) format("woff");
	font-weight: 300;
	font-style: normal;
	unicode-range: U+000-5FF;
}

@font-face {
	font-family: "Poppins";
	src: local("Poppins"), url(./fonts/poppins-400.woff) format("woff");
	font-weight: 400;
	font-style: normal;
	unicode-range: U+000-5FF;
}

@font-face {
	font-family: "Poppins";
	src: local("Poppins"), url(./fonts/poppins-500.woff) format("woff");
	font-weight: 500;
	font-style: normal;
	unicode-range: U+000-5FF;
}

@font-face {
	font-family: "Poppins";
	src: local("Poppins"), url(./fonts/poppins-600.woff) format("woff");
	font-weight: 600;
	font-style: normal;
	unicode-range: U+000-5FF;
}

@font-face {
	font-family: "Poppins";
	src: local("Poppins"), url(./fonts/poppins-700.woff) format("woff");
	font-weight: 700;
	font-style: normal;
	unicode-range: U+000-5FF;
}

@font-face {
	font-family: "Poppins";
	src: local("Poppins"), url(./fonts/poppins-800.woff) format("woff");
	font-weight: 800;
	font-style: normal;
	unicode-range: U+000-5FF;
}

/* Styles */
html,
body {
	height: 100%;
}

:root {
	color-scheme: only light !important;
	color-scheme: light !important;
}
</style>
