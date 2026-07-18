import type { Config } from "tailwindcss";

const config: Config = {
  content: [
    "./src/**/*.{js,ts,jsx,tsx,mdx}",
  ],
  theme: {
    extend: {
      colors: {
        brand: {
          DEFAULT: "#1f3a5f",
          light: "#2c5282",
        },
        accent: {
          DEFAULT: "#16a085",
          light: "#1abc9c",
        },
      },
    },
  },
  plugins: [],
};

export default config;
