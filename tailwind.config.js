/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./templates/**/*.html",
    "./templates/**/**/*.html",
    "./app/templates/**/*.html",
    "./djangocourse/templates/**/*.html",
  ],
  theme: {
    extend: {},
  },
  plugins: [],
}
