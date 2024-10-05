import React, { useEffect, useState } from 'react';

function InstagramEmbed({ postUrl }) {
    const [embedHtml, setEmbedHtml] = useState(null);

    useEffect(() => {
        const fetchEmbedData = async () => {
            try {
                const response = await fetch(
                    `https://graph.facebook.com/v11.0/instagram_oembed?url=${postUrl}&access_token=YOUR_INSTAGRAM_ACCESS_TOKEN`
                );
                const data = await response.json();
                setEmbedHtml(data.html);
            } catch (error) {
                console.error('Failed to load Instagram post:', error);
            }
        };

        fetchEmbedData();
    }, [postUrl]);

    return <div className="instagram-embed" dangerouslySetInnerHTML={{ __html: embedHtml }} />;
}

export default InstagramEmbed;
