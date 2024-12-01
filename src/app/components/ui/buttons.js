"use client";
import React, { useState } from "react";

export function DefaultButton({ text, onClick, type }) {
  const [loading, setloading] = useState(false);
  const handleClick = async (e) => {
    if (type === "submit") return;
    setloading(true);
    e.preventDefault();
    e.stopPropagation();
    setloading(true);
    onClick();
    setloading(false);
  };
  return (
    <button
      disabled={loading}
      type="submit"
      className="group relative w-full flex justify-center py-2 px-4 border border-transparent text-sm font-medium rounded-md text-white bg-accent-background hover:opacity-80 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-accent-background"
      onClick={handleClick}
    >
      {text}
    </button>
  );
}
export function SecondaryButton({ text, onClick }) {
  return (
    <button
      type="submit"
      className="group relative w-full flex justify-center py-2 px-4 border border-transparent text-sm font-medium rounded-md text-white bg-secondary-background hover:opacity-80 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-secondary-background"
    >
      {text}
    </button>
  );
}
