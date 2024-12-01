import { AuthKit, APIkit } from "@/app/api/kits";
import { routes } from "@/app/api/routes";

export const login = async (body) => {
  try {
    const response = await AuthKit.post(routes.login, body);
    const data = response.data;
    console.log(data);
    if (data.status) {
      return data.data;
    }
  } catch (error) {
    if (error.response.data.message === "Email not verified") {
      return "NOT VERIFIED";
    } else {
      throw Error(error.response.data.message);
    }
  }
};
export const register = async (body) => {
  try {
    const response = await AuthKit.post(routes.register, body);
    const data = response.data;
    if (data.status) {
      return data.data;
    } else {
      throw Error(data.message);
    }
  } catch (error) {
    throw Error(error.response.data.message);
  }
};
export const verify = async (body) => {
  try {
    const response = await AuthKit.post(routes.verify, body);
    const data = response.data;
    if (data.status) {
      return response;
    } else {
      throw Error(data.message);
    }
  } catch (error) {
    throw Error(error.response.data.message);
  }
};
export const resendVerify = async (body) => {
  try {
    const response = await AuthKit.post(routes.resendVerify, body);
    const data = response.data;
    if (data.status) {
      return response;
    } else {
      throw Error(data.message);
    }
  } catch (error) {
    throw Error(error.response.data.message);
  }
};
export const reset = async (body) => {
  try {
    const response = await AuthKit.post(routes.reset, body);
    const data = response.data;
    if (data.status) {
      return data.data;
    } else {
      throw Error(data.message);
    }
  } catch (error) {
    throw Error(error.response.data.message);
  }
};
export const password = async (body) => {
  try {
    const response = await AuthKit.post(routes.password, body);
    const data = response.data;
    if (data.status) {
      return data.data;
    } else {
      throw Error(data.message);
    }
  } catch (error) {
    throw Error(error.response.data.message);
  }
};
