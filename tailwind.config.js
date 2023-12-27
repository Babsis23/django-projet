/** @type {import('tailwindcss').Config} */
const colors = require('tailwindcss/colors')

module.exports = {
  content: ["./src/templates/**/*.{html,js}"],
  theme: {
    colors: {
      white: "#F9F9F9",
      black: "#202020",
      bg:"#F7F9FF",
      bg2:"#EDF2FE",
      bg3:"#E1E9FF",
      cmpnt:"#D2DEFF",
      border:"#ABBDF9",
      solid:"##3E63DD",
      primary: "#1F2D5C",
      secondary:"##3A5BC7",
    },
    fontFamily: {
      'poppins': ['Poppins', 'sans-serif'],
      'roboto': ['Roboto', 'sans-serif'],
    },
    extend: {},
  },
  plugins: [],
}