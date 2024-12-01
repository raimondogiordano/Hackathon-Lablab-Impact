"use client";
import React from "react";
import AuthLayout from "../components/layouts/auth";

function Auth({ children }) {
  return <AuthLayout>{children}</AuthLayout>;
}

export default Auth;
