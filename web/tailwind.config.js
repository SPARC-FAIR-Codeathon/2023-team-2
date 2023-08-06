/* eslint-disable no-undef */

/** @type {import('tailwindcss').Config} */
const { fontFamily } = require('tailwindcss/defaultTheme')

// eslint-disable-next-line no-undef
module.exports = {
  content: ['./index.html', './src/**/*.{vue,js,ts,jsx,tsx,mdx,stories.js,stories.mdx}'],
  corePlugins: {
    preflight: false
  },
  plugins: [
    require('tailwindcss-debug-screens'),
    require('@tailwindcss/typography'),
    require('prettier-plugin-tailwindcss')
  ],
  theme: {
    extend: {
      colors: {},
      fontFamily: {
        primary: ['Inter', ...fontFamily.sans]
      }
    }
  }
}
