module.exports = {
  env: {
    browser: true,
    es6: true,
  },
  parserOptions: {
    parser: "babel-eslint",
  },
  extends: [
    "airbnb-base",
    "plugin:vue/recommended",
  ],
  plugins: [
    "vue",
  ],
  rules: {
    "no-console": "off",
    "vue/max-attributes-per-line": [
      2,
      {
        multiline: {
          allowFirstLine: true
        }
      }
    ],
    quotes: ["error", "double"],
    "max-len": ["error", { code: 140, ignoreStrings: true, ignoreUrls: true }],
    "import/no-unresolved": 0,
    "linebreak-style": 0,
    "comma-dangle": 0,
    "space-before-function-paren": 0,
    "import/prefer-default-export": 0,
    "no-unused-expressions": ["error", { allowTernary: true }],
    "no-underscore-dangle": 0,
    "no-param-reassign": 0,
    "object-curly-newline": ["error", { ObjectPattern: "never" }],
    "vue/html-closing-bracket-newline": ["error", {
      singleline: "never",
      multiline: "always"
    }]
  }
  
};


