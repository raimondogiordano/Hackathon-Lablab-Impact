"use client";

import { DoDecrypt, DoEncrypt } from "./encrypter";

export default {
  setItem: (obj, key) => {
    //PROD
    const string = JSON.stringify(obj);
    const encrypt = DoEncrypt(string);
    if (typeof window !== "undefined") {
      window.localStorage.setItem(key, encrypt);
    }
  },

  getItem: (key) => {
    let encrypt = "";
    if (typeof window !== "undefined") {
      encrypt = window.localStorage.getItem(key, encrypt);
    }

    if (!encrypt) {
      return null;
    }
    //PROD
    const string = DoDecrypt(encrypt);
    const obj = JSON.parse(string);
    return obj;
  },

  clear: () => {
    localStorage.clear();
    sessionStorage.clear();
  },

  KEYS: {
    USER: "USER",
    STATE: "STATE",
    REMEMBER_ME: "REMEMBER_ME",
  },
};
