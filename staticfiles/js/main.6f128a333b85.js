// Auto-hide messages after 5 seconds
document.addEventListener("DOMContentLoaded", () => {
    const messages = document.querySelectorAll(".message, .alert")
    if (messages.length > 0) {
        setTimeout(() => {
            messages.forEach((message) => {
                message.style.opacity = "0"
                setTimeout(() => {
                    message.style.display = "none"
                }, 500)
            })
        }, 5000)
    }
})

// Mobile navigation toggle
function mobileNavToggle() {
    const navLinks = document.querySelector(".nav-links")
    if (navLinks) {
        navLinks.classList.toggle("show")
    }
}

// Calendar functionality
function initCalendar() {
    const calendarEl = document.getElementById("calendar")
    if (!calendarEl) return

    if (typeof FullCalendar !== "undefined") {
        const eventsData = document.getElementById("calendarEvents")
        let events = []

        if (eventsData) {
            try {
                events = JSON.parse(eventsData.textContent)
            } catch (e) {
                console.error("Error parsing calendar events:", e)
            }
        }

        const calendar = new FullCalendar.Calendar(calendarEl, {
            initialView: "dayGridMonth",
            headerToolbar: {
                left: "prev,next today",
                center: "title",
                right: "dayGridMonth,timeGridWeek,timeGridDay",
            },
            events: events,
            eventClick: (info) => {
                alert(
                    "Event: " +
                    info.event.title +
                    "\n" +
                    "Description: " +
                    (info.event.extendedProps.description || "No description"),
                )
            },
        })

        calendar.render()
    } else {
        const date = new Date()
        const month = date.toLocaleString("default", { month: "long" })
        const year = date.getFullYear()

        const calendarHeader = document.createElement("h2")
        calendarHeader.textContent = `${month} ${year}`
        calendarEl.appendChild(calendarHeader)

        const message = document.createElement("p")
        message.textContent = "Calendar library not loaded. Please check your internet connection."
        message.className = "text-muted"
        calendarEl.appendChild(message)
    }
}

// Email functionality
function initEmailList() {
    const emailListEl = document.getElementById("email-list")
    if (!emailListEl) return

    const emailItems = document.querySelectorAll(".email-item")
    emailItems.forEach((item) => {
        item.addEventListener("click", function () {
            emailItems.forEach((el) => el.classList.remove("bg-light"))
            this.classList.add("bg-light")
            console.log("Email clicked:", this.querySelector(".fw-bold").textContent)
        })
    })
}

// Initialize components
document.addEventListener("DOMContentLoaded", () => {
    initCalendar()
    initEmailList()

    const forms = document.querySelectorAll("form")
    forms.forEach((form) => {
        form.addEventListener("submit", (event) => {
            const requiredFields = form.querySelectorAll("[required]")
            let isValid = true

            requiredFields.forEach((field) => {
                if (!field.value.trim()) {
                    isValid = false
                    field.classList.add("is-invalid")
                } else {
                    field.classList.remove("is-invalid")
                }
            })

            if (!isValid) {
                event.preventDefault()
                alert("Please fill in all required fields")
            }
        })
    })
})
