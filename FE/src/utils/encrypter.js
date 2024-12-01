import CryptoJS from "crypto-js";
import { constants } from "./constant";
const env = "DEV";
var key = constants[env].ENCRYPTION_KEY;

export const DoEncrypt = (text) => {
  var encrypted = CryptoJS.AES.encrypt(text, key).toString();
  return encrypted;
};
export const DoDecrypt = (cipher) => {
  var decrypted = CryptoJS.AES.decrypt(cipher, key).toString(CryptoJS.enc.Utf8);
  return decrypted;
};
