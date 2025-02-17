import { useContext, useState, useEffect } from "react";
import { useNavigate } from "react-router-dom";
import AuthContext from "../context/AuthContext";
import axios from "axios";

const Profile = () => {
    const { authTokens, user } = useContext(AuthContext);
    const navigate = useNavigate();
    
    const [profile, setProfile] = useState({
        first_name: "",
        last_name: "",
        department: "", // For Supervisor
        programme: "", // For Student Lead
        supervisor: "", // For Student Lead (stores ID)
    });

    const [supervisors, setSupervisors] = useState([]); // Store fetched supervisors
    const [loading, setLoading] = useState(false); // Track form submission status

    // Fetch supervisors when the user is a student
    useEffect(() => {
        if (user.role === "student") {
            axios
                .get("https://project-pms-kyu.vercel.app/user/supervisors/", {
                    headers: { Authorization: `Bearer ${authTokens.access}` },
                })
                .then((response) => {
                    setSupervisors(response.data);
                })
                .catch((error) => {
                    console.error("Error fetching supervisors:", error);
                });
        }
    }, [user.role, authTokens]);

    // Handle input change
    const handleChange = (e) => {
        const { name, value } = e.target;
        setProfile((prev) => ({
            ...prev,
            [name]: value,
        }));
    };

    // Handle form submission
    const handleSubmit = (e) => {
        e.preventDefault();

        if (!authTokens) {
            navigate("/login");
            return;
        }

        setLoading(true); // Disable button and change text to "Processing..."

        const requestData = {
            first_name: profile.first_name,
            last_name: profile.last_name,
            ...(user.role === "supervisor"
                ? { department: profile.department }
                : { programme: profile.programme, supervisor: profile.supervisor }),
        };

        const url =
            user.role === "supervisor"
                ? "https://project-pms-kyu.vercel.app/user/create-profile/supervisor/"
                : "https://project-pms-kyu.vercel.app/user/create-profile/studentlead/";

        axios
            .post(url, requestData, {
                headers: {
                    Authorization: `Bearer ${authTokens.access}`,
                    "Content-Type": "application/json",
                },
            })
            .then(() => {
                navigate("/home");
            })
            .catch((error) => {
                console.error("Error creating profile:", error.response ? error.response.data : error);
                setLoading(false); // Re-enable button on error
            });
    };

    const handleCancel = () => navigate("/");

    return (
        <div className="max-w-lg mx-auto p-6 bg-white rounded-lg shadow-lg">
            <h2 className="text-2xl font-bold mb-4 text-center">Create Your Profile</h2>
            <form onSubmit={handleSubmit} className="space-y-4">
                {/* First Name */}
                <div className="flex flex-col">
                    <label className="text-sm font-semibold text-gray-700" htmlFor="first_name">
                        First Name:
                    </label>
                    <input
                        type="text"
                        name="first_name"
                        value={profile.first_name}
                        onChange={handleChange}
                        id="first_name"
                        className="mt-2 p-2 border border-gray-300 rounded-md focus:ring-2 focus:ring-blue-500"
                        required
                    />
                </div>

                {/* Last Name */}
                <div className="flex flex-col">
                    <label className="text-sm font-semibold text-gray-700" htmlFor="last_name">
                        Last Name:
                    </label>
                    <input
                        type="text"
                        name="last_name"
                        value={profile.last_name}
                        onChange={handleChange}
                        id="last_name"
                        className="mt-2 p-2 border border-gray-300 rounded-md focus:ring-2 focus:ring-blue-500"
                        required
                    />
                </div>

                {/* Supervisor Role - Department Input */}
                {user.role === "supervisor" && (
                    <div className="flex flex-col">
                        <label className="text-sm font-semibold text-gray-700" htmlFor="department">
                            Department:
                        </label>
                        <input
                            type="text"
                            name="department"
                            value={profile.department}
                            onChange={handleChange}
                            id="department"
                            className="mt-2 p-2 border border-gray-300 rounded-md focus:ring-2 focus:ring-blue-500"
                            required
                        />
                    </div>
                )}

                {/* Student Role - Programme & Supervisor Select */}
                {user.role === "student" && (
                    <>
                        <div className="flex flex-col">
                            <label className="text-sm font-semibold text-gray-700" htmlFor="programme">
                                Programme:
                            </label>
                            <input
                                type="text"
                                name="programme"
                                value={profile.programme}
                                onChange={handleChange}
                                id="programme"
                                className="mt-2 p-2 border border-gray-300 rounded-md focus:ring-2 focus:ring-blue-500"
                                required
                            />
                        </div>

                        <div className="flex flex-col">
                            <label className="text-sm font-semibold text-gray-700" htmlFor="supervisor">
                                Supervisor:
                            </label>
                            <select
                                name="supervisor"
                                value={profile.supervisor}
                                onChange={handleChange}
                                id="supervisor"
                                className="mt-2 p-2 border border-gray-300 rounded-md focus:ring-2 focus:ring-blue-500"
                                required
                            >
                                <option value="">Select a Supervisor</option>
                                {supervisors.length > 0 ? (
                                    supervisors.map((sup) => (
                                        <option key={sup.user_id} value={sup.user_id}>
                                            {sup.first_name} {sup.last_name} - {sup.department}
                                        </option>
                                    ))
                                ) : (
                                    <option disabled>No supervisors available</option>
                                )}
                            </select>
                        </div>
                    </>
                )}

                {/* Buttons */}
                <div className="flex space-x-4">
                    <button
                        type="submit"
                        className={`w-full py-2 mt-4 rounded-md text-white ${
                            loading ? "bg-gray-400 cursor-not-allowed" : "bg-blue-600 hover:bg-blue-700"
                        }`}
                        disabled={loading}
                    >
                        {loading ? "...Processing..." : "Create Profile"}
                    </button>
                    <button
                        type="button"
                        onClick={handleCancel}
                        className="w-full py-2 mt-4 bg-gray-600 text-white rounded-md hover:bg-gray-700"
                    >
                        Cancel
                    </button>
                </div>
            </form>
        </div>
    );
};

export default Profile;
