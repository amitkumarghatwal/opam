@1

package "P4" {
  version     = "2"
  description = "Testing transitive closure"
  urls        = [ "http://www.ocamlpro.com/pub/p4.tar.gz" ]
  depends     = "P2, P3"
}
