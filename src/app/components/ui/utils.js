import React from "react";

export const Hug = ({ children, gap }) => {
  return (
    <div className={`flex gap-${gap || "2"}  w-full items-center my-0`}>
      {children}
    </div>
  );
};
