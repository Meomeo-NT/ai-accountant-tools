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
          DEFAULT: "#0d9488",
          light: "#14b8a6",
        },
        "accent-text": {
          DEFAULT: "#0f766e",
        },
        neutral: {
          50: "#f8fafc",
          100: "#f1f5f9",
          200: "#e2e8f0",
          600: "#475569",
          900: "#0f172a",
        },
      },
    },
  },
  plugins: [],
};

export default config;
