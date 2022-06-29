/** @type {import('tailwindcss').Config} */
module.exports = {
  purge: {
    enabled: true,
    content: ['../src/web/templates/web/**/*.html'],
  },
  darkMode: "class", // or 'media' or 'class'
  theme: {
      extend: {
          width: {
              690: "690px",
              500: "500px" // half of 690
          },
          minWidth: {
              0: "0",
              input: "500px",
          },
          fontSize: {
              title: "18px",
          },
          textColor: {
              staleBlue: "#1a0dab",
          },
          boxShadow: {
              'info_box': 'var(--info-box-shadow)',
          },
          colors: {
              'info_box_bg': 'var(--info-box-bg)',
              'info_box_cl': 'var(--info-box-cl)',
              'info_box_cl2': 'var(--info-box-cl2)',

              'page_bg': 'var(--page-bg)',

              'rs_bg': 'var(--rs-bg)',
              'rs_tl': 'var(--rs-tl)',
              'rs_ds': 'var(--rs-ds)',

              'header_bg': 'var(--header-bg)',
          }
      },
  },
  variants: {
      extend: {},
  },
  plugins: [],
};