module.exports = {
    "env": {
        "browser": true,
        "es6": true
    },
    "parserOptions": {
        "parser": "babel-eslint"
    },
    "extends": [
        "airbnb-base",
        "plugin:vue/recommended"
    ],
    "plugins": [
        "vue"
    ],
    "rules": {
        "quotes": [2, "double", { "avoidEscape": true }]
    }
};