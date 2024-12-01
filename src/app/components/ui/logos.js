"use client";

import React from "react";

export function LogoAuth({ theme }) {
  return (
    <div>
      <img
        src={`/assets/logo-${theme}.png`}
        alt="Diary logo"
        className={`h-[30px] w-auto mt-10 mx-auto object-contain`}
      />
    </div>
  );
}
export function LogoHeader({ theme }) {
  return (
    <div>
      <img
        src={`/assets/logo-${theme}.png`}
        alt="Diary logo"
        className={`h-[20px] w-auto mx-auto object-contain`}
      />
    </div>
  );
}
