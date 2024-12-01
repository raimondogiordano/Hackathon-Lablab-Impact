/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./src/pages/**/*.{js,ts,jsx,tsx,mdx}",
    "./src/components/**/*.{js,ts,jsx,tsx,mdx}",
    "./src/app/**/*.{js,ts,jsx,tsx,mdx}",
  ],
  darkMode: "selector",
  theme: {
    extend: {
      backgroundImage: {
        "gradient-radial": "radial-gradient(var(--tw-gradient-stops))",
        "gradient-conic":
          "conic-gradient(from 180deg at 50% 50%, var(--tw-gradient-stops))",
      },
      colors: {
        light: {
          background: "#ffffff",
          text: "#000000",
          border: "#c2c2c2",
        },
        dark: {
          background: "#000",
          text: "#ffffff",
          border: "#222",
        },
        accent: {
          background: "#414141",
          text: "#ffffff",
          linkDark: "#007399",
          link: "#002933",
        },
        utils: {
          error: "#b30000",
          success: "#00ff00",
          warning: "#ffcc00",
          action: "#0041414199",
        },
      },
    },
  },
  plugins: [],
};
