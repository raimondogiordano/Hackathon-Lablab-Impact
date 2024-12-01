"use client";
import { register } from "@/app/api";
import { DefaultButton } from "@/app/components/ui/buttons";
import { Input, InputEnd, InputStart } from "@/app/components/ui/inputs";
import Link from "next/link";
import { useState } from "react";

import { FaGoogle, FaApple } from "react-icons/fa";

export default function Signup() {
  const [user, setuser] = useState({
    name: "",
    surname: "",
    email: "",
    password: "",
    ruolo: "",
  });

  const handleChange = (e) => {
    setuser({ ...user, [e.target.name]: e.target.value });
  };
  const handleSubmit = async (e) => {
    try {
      e.preventDefault();
      e.stopPropagation();
      const userValue = { ...user };
      delete userValue.ruolo;
      const response = await register(userValue);

      // const data = await createPlayer({
      //   userId: response._id,
      //   role: user.ruolo,
      //   name: user.name + " " + user.surname,
      // });
      setuser({
        name: "",
        surname: "",
        email: "",
        password: "",
        ruolo: "",
      });
      // if (data) {
        alert(
          "Registrazione avvenuta con successo riceverai una mail per verificare il tuo account"
        );
      // }
    } catch (error) {
      alert(error.message);
    }
  };
  return (
    <div className="w-full max-w-md p-8 space-y-8 bg-light-background rounded shadow dark:bg-dark-background border-light-border dark:border-dark-border border-[0.5px]">
      <h2 className="text-2xl font-bold text-center text-gray-900 dark:text-white">
        Sign Up
      </h2>
      <form className="mt-8 space-y-6" onSubmit={handleSubmit}>
        <input type="hidden" name="remember" value="true" />
        <div className="rounded-md shadow-sm -space-y-px">
          <InputStart
            type={"text"}
            placeholder={"Nome"}
            label={"Name"}
            name="name"
            value={user.name}
            onChange={handleChange}
            required={true}
          />
          <Input
            type={"text"}
            placeholder={"Cognome"}
            label={"Cognome"}
            name="surname"
            value={user.surname}
            onChange={handleChange}
            required={true}
          />
          <Input
            type={"Email"}
            placeholder={"Email"}
            label={"Email address"}
            name="email"
            value={user.email}
            onChange={handleChange}
            required={true}
          />
          <InputEnd
            type={"password"}
            placeholder={"Password"}
            label={"Password"}
            name="password"
            value={user.password}
            onChange={handleChange}
            required={true}
          />
          <select
            name="ruolo"
            value={user.ruolo}
            onChange={handleChange}
            required
            className="w-full my-6 text-[12px] border border-light-border dark:border-dark-border bg-light-background dark:bg-dark-background rounded-md p-2"
          >
            <option value={""}>Seleziona il tuo ruolo</option>
            <option value={"P"}>Portiere</option>
            <option value={"D"}>Difensore</option>
            <option value={"C"}>Centrocampista</option>
            <option value={"A"}>Attaccante</option>
          </select>
        </div>
        <div>
          <DefaultButton type={"submit"} text={"Sign Up"} />
        </div>
      </form>
      <hr className="w-[30%] border-1 border-light-border dark:border-dark-border mx-auto" />
      {/* <div className="flex gap-4 w-fit mx-auto">
        <button className="p-3 rounded-lg border border-light-border dark:border-dark-border">
          <FaGoogle />
        </button>
        <button className="p-3 rounded-lg border border-light-border dark:border-dark-border">
          <FaApple />
        </button>
      </div> */}
      <div className="text-sm text-center">
        <Link href="/auth/login">Already have an account? Sign In</Link>
      </div>
    </div>
  );
}
