"use client";
import React, { useEffect, useState } from "react";
import { BasicModal } from "../../ui/modals";
import useModal from "@/app/hooks/useModal";
import moment from "moment";
import useRole from "@/app/hooks/useRole";

const MatchList = ({ matches, onCreateMatch, onClickMatch }) => {
  const modal = useModal();
  const { isAdmin } = useRole();
  const onCreateMatchNew = () => {
    modal.openModal();
  };
  const [data, setdata] = useState({ date: Date.now(), location: "Mazzone" });
  const [loading, setloading] = useState(true);
  useEffect(() => {
    setloading(false);
  }, []);

  const handleChange = (e) => {
    setdata({ ...data, [e.target.name]: e.target.value });
  };
  return (
    <div className="flex flex-col h-full bg-light-background dark:bg-dark-background text-light-text dark:text-dark-text p-4 rounded-lg border border-light-border dark:border-dark-border">
      {/* Lista dei Match */}
      {!loading && (
        <>
          <div className="flex-1 overflow-y-auto mb-4">
            <ul>
              {matches.map((match, index) => (
                <li
                  key={index}
                  onClick={() => onClickMatch(match._id)}
                  className="p-4 mb-2 border border-light-border dark:border-dark-border rounded-lg bg-light-background dark:bg-dark-background block cursor-pointer"
                >
                  <div className="flex justify-between">
                    <span>
                      <span className={"font-bold"}>
                        {moment(match.date.split(".")[0]).format(
                          "DD/MM/YY HH:mm"
                        )}
                      </span>
                      <br />
                      <span>{match.location}</span>
                    </span>
                    <span>{match.result}</span>
                  </div>
                </li>
              ))}
            </ul>
          </div>

          {/* Bottone per Creare un Nuovo Match */}
          {isAdmin && (
            <button
              onClick={onCreateMatchNew}
              className="mt-auto p-3 bg-accent-background text-accent-text rounded-lg"
            >
              Crea Nuovo Match
            </button>
          )}
          <BasicModal modal={modal}>
            <div className="flex flex-col gap-4 p-4">
              <input
                type="hidden"
                id="timezone"
                name="timezone"
                value="02:00"
              />
              <input
                type="datetime-local"
                value={data.date}
                name="date"
                onChange={handleChange}
                className="border border-light-border dark:border-dark-border bg-light-background dark:bg-dark-background text-light-text dark:text-dark-text rounded-md p-2 "
              />
              <input
                type="text"
                value={data.location}
                name="location"
                onChange={handleChange}
                placeholder="Campo"
                className="border border-light-border dark:border-dark-border bg-light-background dark:bg-dark-background text-light-text dark:text-dark-text rounded-md p-2"
              />
              <button
                onClick={() => onCreateMatch(data)}
                className="p-3 bg-accent-background text-accent-text rounded-lg "
              >
                Crea Match
              </button>
            </div>
          </BasicModal>
        </>
      )}
    </div>
  );
};

export default MatchList;
