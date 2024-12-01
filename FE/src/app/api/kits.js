import axios from "axios";
import { constants } from "@/utils/constant";

const env = "DEV";
export const AuthKit = axios.create({
  baseURL: constants[env].AUTH_SERVER_URL,
  timeout: 100000,
});
AuthKit.interceptors.request.use(
  async (config) => {
    config.headers["x-tenant"] = constants[env].TENANT_ID;
    return config;
  },
  (error) => {
    Promise.reject(error);
  }
);
export const APIkit = axios.create({
  baseURL: constants[env].SERVER_URL + constants[env].API_BASE_URL,
  timeout: 100000,
});
// const findToken = () => {
//   const user = localStorageManager.getItem(localStorageManager.KEYS.USER);
//   return user.access_token;
// };

// APIkit.interceptors.request.use(
//   async (config) => {
//     const token = findToken();

//     if (token) {
//       config.headers.Authorization = `Bearer ${token}`;
//       config.headers["x-tenant"] = constants[env].TENANT_ID;
//     } else {
//       throw Error("Token is not valid");
//     }
//     return config;
//   },
//   (error) => {
//     Promise.reject(error);
//   }
// );

const post = async (path, body) => {
  try {
    const response = await APIkit.post(path, body);
    const data = response.data;
    if (data.status) {
      return data.data;
    } else {
      throw Error(data.message);
    }
  } catch (error) {
    throw Error(error.message);
  }
};
const get = async (path) => {
  try {
    const response = await APIkit.get(path);
    const data = response.data;
    if (data.status) {
      return data.data;
    } else {
      throw Error(data.message);
    }
  } catch (error) {
    throw Error(error.message);
  }
};
const multipart_get = async (path) => {
  try {
    const response = await APIkit.get(path, { responseType: "blob" });
    const data = response.data;
    if (response.status) {
      return data;
    } else {
      throw Error(data);
    }
  } catch (error) {
    throw Error(error.message);
  }
};

const multipart_post = async (path, body) => {
  try {
    const response = await APIkit.post(
      path,
      { path: body },
      { responseType: "blob" }
    );
    const data = response.data;
    if (response.status) {
      return data;
    } else {
      throw Error(data);
    }
  } catch (error) {
    throw Error(error.message);
  }
};
const patch = async () => {};
const _delete = async (path) => {
  try {
    const response = await APIkit.delete(path);
    const data = response.data;
    if (data.status) {
      return data.data;
    } else {
      throw Error(data.message);
    }
  } catch (error) {
    throw Error(error.message);
  }
};
const put = async (path, body) => {
  try {
    const response = await APIkit.put(path, body);
    const data = response.data;
    if (data.status) {
      return data.data;
    } else {
      throw Error(data.message);
    }
  } catch (error) {
    throw Error(error.message);
  }
};

const o_post = async (path, body) => {
  try {
    const response = await AuthKit.post(path, body);
    const data = response.data;
    if (data.status) {
      return data.data;
    } else {
      throw Error(data.message);
    }
  } catch (error) {
    throw Error(error.message);
  }
};
const o_get = async (path) => {
  try {
    const response = await AuthKit.get(path);
    const data = response.data;
    if (data.status) {
      return data.data;
    } else {
      throw Error(data.message);
    }
  } catch (error) {
    throw Error(error.message);
  }
};

const o_patch = async () => {};
const o_delete = async () => {};
const o_put = async () => {};
export const kit = {
  post,
  get,
  patch,
  _delete,
  put,
  o_post,
  o_get,
  o_patch,
  o_delete,
  o_put,
  multipart_get,
  multipart_post,
};
