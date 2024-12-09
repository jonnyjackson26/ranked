import { useEffect, useState } from 'react';
import './StatsPage.css';
import { FaFacebook, FaTwitter, FaInstagram, FaLinkedin } from 'react-icons/fa';
import Navbar from '../../components/Navbar/Navbar';

function StatsPage() {
    const [stats, setStats] = useState(null);

    useEffect(() => {
        async function fetchStats() {
            const res = await fetch("/get-stats/", {
                credentials: "same-origin",
            });

            if (res.ok) {
                const data = await res.json();
                setStats(data);
            }
        }

        fetchStats();
    }, []);

    const handleShare = (platform, message) => {
        const urls = {
            facebook: `https://www.facebook.com/sharer/sharer.php?u=${encodeURIComponent(message)}`,
            twitter: `https://twitter.com/intent/tweet?text=${encodeURIComponent(message)}`,
            instagram: '#', // Instagram sharing via URL is not available; placeholder
            linkedin: `https://www.linkedin.com/sharing/share-offsite/?url=${encodeURIComponent(message)}`,
        };
        window.open(urls[platform], '_blank');
    };

    return (
        <>
        <Navbar />
        <div className="stats-page">
            <h1>🎉 Your Amazing Stats! 🎉</h1>
            <p>Congratulations on your incredible achievements! Here's how you stack up:</p>

            {stats ? (
                <div className="stats-container">
                    {stats.map((stat, index) => (
                        <div key={index} className="stat-card">
                            <h2>{stat.title}</h2>
                            <p>{stat.description}</p>
                            <div className="share-buttons">
                                <button onClick={() => handleShare('facebook', stat.shareMessage)}>
                                    <FaFacebook /> Share
                                </button>
                                <button onClick={() => handleShare('twitter', stat.shareMessage)}>
                                    <FaTwitter /> Tweet
                                </button>
                                <button onClick={() => handleShare('instagram', stat.shareMessage)}>
                                    <FaInstagram /> Share
                                </button>
                                <button onClick={() => handleShare('linkedin', stat.shareMessage)}>
                                    <FaLinkedin /> Share
                                </button>
                            </div>
                        </div>
                    ))}
                </div>
            ) : (
                <p>Loading your stats...</p>
            )}
        </div>
        </>
    );
}

export default StatsPage;
