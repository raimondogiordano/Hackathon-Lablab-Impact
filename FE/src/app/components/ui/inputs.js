import React from "react";

export function InputStart({
  label,
  id,
  name,
  type,
  autoComplete,
  required,
  placeholder,
  value,
  onChange,
}) {
  return (
    <div>
      <label htmlFor="email-address" className="sr-only">
        {label}
      </label>
      <input
        id={id}
        name={name}
        type={type}
        autoComplete={autoComplete}
        required={required}
        className="appearance-none rounded-none rounded-t-md relative block w-full px-3 py-2 border border-light-border dark:border-dark-border placeholder-gray-500 text-light-text dark:text-dark-text focus:outline-none sm:text-sm bg-light-background dark:bg-dark-background"
        placeholder={placeholder}
        value={value}
        onChange={onChange}
      />
    </div>
  );
}
export function Input({
  label,
  id,
  name,
  type,
  autoComplete,
  required,
  placeholder,
  value,
  onChange,
}) {
  return (
    <div>
      <label htmlFor="email-address" className="sr-only">
        {label}
      </label>
      <input
        id={id}
        name={name}
        type={type}
        autoComplete={autoComplete}
        required={required}
        className="appearance-none rounded-none relative block w-full px-3 py-2 border border-light-border dark:border-dark-border placeholder-gray-500 text-light-text dark:text-dark-text focus:outline-none sm:text-sm bg-light-background dark:bg-dark-background"
        placeholder={placeholder}
        value={value}
        onChange={onChange}
      />
    </div>
  );
}
export function InputRounded({
  label,
  id,
  name,
  type,
  autoComplete,
  required,
  placeholder,
  value,
  onChange,
}) {
  return (
    <div>
      <label htmlFor="email-address" className="sr-only">
        {label}
      </label>
      <input
        id={id}
        name={name}
        type={type}
        autoComplete={autoComplete}
        required={required}
        className="appearance-none rounded-md relative block w-full px-3 py-2 border border-light-border dark:border-dark-border placeholder-gray-500 text-light-text dark:text-dark-text focus:outline-none sm:text-sm bg-light-background dark:bg-dark-background"
        placeholder={placeholder}
        value={value}
        onChange={onChange}
      />
    </div>
  );
}

export function InputEnd({
  label,
  id,
  name,
  type,
  autoComplete,
  required,
  placeholder,
  value,
  onChange,
}) {
  return (
    <div>
      <label htmlFor="email-address" className="sr-only">
        {label}
      </label>
      <input
        id={id}
        name={name}
        type={type}
        autoComplete={autoComplete}
        required={required}
        className="appearance-none rounded-none rounded-b-md relative block w-full px-3 py-2 border border-light-border dark:border-dark-border placeholder-gray-500 text-light-text dark:text-dark-text focus:outline-none sm:text-sm bg-light-background dark:bg-dark-background"
        placeholder={placeholder}
        value={value}
        onChange={onChange}
      />
    </div>
  );
}
