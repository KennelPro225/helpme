/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./templates/**/*.html"],
  theme: {
    fontFamily: {
      sans: ["montserrat"],
    },
    letterSpacing: {
      tightest: "-.075em",
      tighter: "-.05em",
      tight: "-.025em",
      normal: "0",
      wide: ".025em",
      wider: ".05em",
      widest: ".1em",
      widest: ".25em",
    },
    extend: {
      height: {
        2002: "96vh",
      },

      width: {
        2300: "90vw",
      },

      margin: {
        3122: "23px",
      },
      minHeight: {
        2002: "10vh",
        111: "30",
      },
    },
  },
  plugins: [],
};
