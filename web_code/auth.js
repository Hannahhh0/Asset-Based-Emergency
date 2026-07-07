import { getAuth } from "firebase/auth";
import { getFirestore, doc, getDoc } from "firebase/firestore";

export async function requireStaff() {
    const auth = getAuth();
    const db = getFirestore();

    const user = auth.currentUser;

    if (!user) {
        window.location.href = "staffpage.html";
        return null;
    }

    const snap = await getDoc(doc(db, "authorizedStaff", user.email));

    if (!snap.exists()) {
        await auth.signOut();
        window.location.href = "staffpage.html";
        return null;
    }

    return snap.data();
}