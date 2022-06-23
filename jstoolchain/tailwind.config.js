/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [],
  theme: {
    extend: {},
  },
  purge: {
    enabled: true,
    content: ['../src/web/templates/web/**/*.html'],
  },
  plugins: [],
}
