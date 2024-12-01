import React, { useState } from "react";
import { IoClose } from "react-icons/io5";
export const BasicModal = ({ children, modal }) => {
  const closeModal = () => {
    modal.closeModal();
  };

  return (
    <>
      {modal.isOpen && (
        <div className="fixed inset-0 flex items-center justify-center z-50">
          <div
            onClick={closeModal}
            className="fixed inset-0 bg-black opacity-50"
          ></div>
          <div className="bg-light-background dark:bg-dark-background rounded-lg p-6 z-10 relative text-light-text dark:text-dark-text border-light-border dark:border-dark-border border-[0.5px] min-w-[90%] lg:min-w-[40%] md:min-w-[60%] overflow-auto max-h-[90%]">
            <button
              className="absolute top-0 right-0 m-4 text-gray-500 hover:text-gray-700"
              onClick={closeModal}
            >
              <IoClose />
            </button>
            {children}
          </div>
        </div>
      )}
    </>
  );
};
export const OffsetLeftModal = ({ children, modal }) => {
  const closeModal = () => {
    modal.closeModal();
  };

  return (
    <>
      {modal.isOpen && (
        <div className="fixed inset-0 flex items-center justify-start z-50">
          <div
            onClick={closeModal}
            className="fixed inset-0 bg-black opacity-50"
          ></div>
          <div className="bg-light-background dark:bg-dark-background h-full p-6 z-10 relative text-light-text dark:text-dark-text border-light-border dark:border-dark-border border-[0.5px] min-w-[90%] lg:min-w-[30%] overflow-auto max-h-[100%]">
            <button
              className="absolute top-0 right-0 m-4 text-gray-500 hover:text-gray-700 "
              onClick={closeModal}
            >
              <IoClose />
            </button>
            {children}
          </div>
        </div>
      )}
    </>
  );
};
