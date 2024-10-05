import { defineStore } from "pinia";
import axios from "axios";

export const useMainStore = defineStore("main", {
    state: () => ({
        transcriptData: "",
        flashcardData: [],
    }),
    actions: {
        addTranscript(data) {
            if (data != "") {
                this.transcriptData = data;
            }
        },
        async getPDF() {
            console.log("Fetching")
            try {
                const response = await axios.get(
                    `https://539fc295-8d05-40c6-9cbe-ffdde1f6e2da-00-28yls8lil54ba.janeway.replit.dev/v1/get_pdf/${this.transcriptData}`,
                    { responseType: 'blob' } // !!!
                )
                const blob = new Blob([response.data], { type: 'application/pdf' });
                const urlBlob = window.URL.createObjectURL(blob);

                // Create a link element to trigger the download
                const a = document.createElement('a');
                a.href = urlBlob;
                a.download = 'your_file.pdf'; // Specify the file name
                document.body.appendChild(a);
                a.click(); // Programmatically click the link to trigger the download
                a.remove(); // Remove the link from the document

                // Clean up the URL object
                window.URL.revokeObjectURL(urlBlob);

            } catch (error) {
                console.error(error);
            }
        },

        async getCheatSheet() {
            console.log("Fetching")
            try {
                const response = await axios.get(
                    `https://539fc295-8d05-40c6-9cbe-ffdde1f6e2da-00-28yls8lil54ba.janeway.replit.dev/v1/cheatsheet/${this.transcriptData}`,
                    { responseType: 'blob' } // !!!
                ).then((response) => {
                    window.open(URL.createObjectURL(response.data));
                })

            } catch (error) {
                console.error(error);
            }
        },

        async getFlashCards() {
            this.flashcardData = [];
            console.log("Getting Flashcards");
            try {
                const response = await axios.get(
                    `https://539fc295-8d05-40c6-9cbe-ffdde1f6e2da-00-28yls8lil54ba.janeway.replit.dev/v1/flashcard/${this.transcriptData}`)
                    this.flashcardData = response.data
            } catch (error) {
                console.error(error);
            }
        }

    },

})