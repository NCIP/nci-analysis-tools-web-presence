function termDisplay(Glossary) {
    // pass in an object with the key/value pair of terms
    /**
        {
            "fullName": "Term Name",
            "definition": "definition text"
        }
    **/

    var custom_po_tmpl = "<div class='popover' role='tooltip'><div class='arrow'></div><h3 class='popover-title'></h3><div class='popover-content'></div></div>";

  var $self = $(this);
  var dTerm = $self.attr('data-term');
  if (typeof Glossary[dTerm] === "undefined") return;
  var definition = Glossary[dTerm].definition;
  var term = Glossary[dTerm].fullName;

  if (definition || term) {
    $self.popover(
      {
        template: custom_po_tmpl,
        container: 'body',
        trigger: 'manual',
        placement: 'top',
        title: term,
        content: definition}
    ).on('mouseout', function () {
      $self.popover('hide');
      $self.popover('destroy');
    });

    $self.popover();
    $self.popover('show');
  }
}
