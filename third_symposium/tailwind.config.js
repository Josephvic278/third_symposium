/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ['./app/templates/*.html','./users/templates/*.html', './app/static/js/*.js'],
  theme: {
    extend: {
        colors: {
        'silverR': '#c0c0c0',
        'redD': '#dd0000',
        'DarkOrange': '#ee6600',
      },
    },
  },
  plugins: [],
}
