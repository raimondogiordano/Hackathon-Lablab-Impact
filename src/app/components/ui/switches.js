import React from "react";
import "./styles/switch.css";
import Link from "next/link";
export function RoundedSwitch({ onChange, checked }) {
  return (
    <label className="switch">
      <input type="checkbox" checked={checked} onChange={onChange} />
      <span className="slider round"></span>
    </label>
  );
}

const pages = [
  {
    name: "Note",
    link: "/dashboard/note",
  },
  {
    name: "Chat",
    link: "/dashboard/chat",
  },
];
export function TabSwitch({ onClick }) {
  return (
    <ul className="flex flex-wrap text-sm font-medium text-center text-light-text dark:text-dark-text border-light-border dark:border-dark-border text-[10px] pl-2">
      {pages.map((page) => (
        <li className="me-2">
          <Link
            href={page.link}
            className="inline-block p-2 rounded-lg hover:text-accent-text hover:bg-accent-background dark:hover:bg-accent-background dark:hover:text-accent-text"
          >
            {page.name}
          </Link>
        </li>
      ))}
    </ul>
  );
}
