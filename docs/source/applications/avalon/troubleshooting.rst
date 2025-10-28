=========================================
Troubleshooting Various Avalon Wonky-ness
=========================================

-----------------------------------
Understanding Permissions in Avalon
-----------------------------------

In Avalon, all files and processes should be owned by :code:`app.app`.

However, since most operations run as :code:`root`, permissions can easily become inconsistent—especially if mount
options are not set correctly.

When this happens, files may end up being owned by :code:`root.root`, causing issues with access or functionality.

**Fix:**
Ensure the correct mount options are added to the container configuration through Kubernetes (Kube) or Rancher so that
ownership defaults to :code:`app.app`.

--------------------------------
Hacking Around Avalon Wonky-ness
--------------------------------

The :code:`ingest` and :code:`dropbox` mounts in the *access* environment are essentially placeholders—they appear as
empty directories because they’re not real mounts.

If you need to adjust ownership or permissions, you can usually do this by running as :code:`root` within a Docker
container attached to the same namespace. Doug typically handles this by using the workflow pod to perform such
operations.

**Tip:**
Always double-check which namespace and mounts you’re working with before making permission changes, to avoid affecting
production volumes.
