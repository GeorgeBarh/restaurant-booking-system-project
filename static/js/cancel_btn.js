document.addEventListener("DOMContentLoaded", function () {
    const cancelModal = document.getElementById("cancelModal");
    const cancelForm = document.getElementById("cancelForm");

    cancelModal.addEventListener("show.bs.modal", function (event) {
        const button = event.relatedTarget;
        const bookingId = button.getAttribute("data-booking-id");
        const actionUrl = `/reservations/cancel/${bookingId}/`;

        if (cancelForm) {
            cancelForm.setAttribute("action", actionUrl);
        }
    });
});